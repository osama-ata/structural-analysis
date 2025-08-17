from typing import cast

import numpy as np
import pytest

from structural_analysis.column_theory import ColumnTheory


class TestColumnTheory:
    """Test suite for ColumnTheory class with comprehensive Euler buckling tests."""

    def setup_method(self):
        """Set up test fixtures."""
        self.column = ColumnTheory()
        # Standard test parameters for steel column
        self.length = 3.0  # 3 meters
        self.E = 200e9  # 200 GPa (steel)
        self.second_moment = 8.33e-6  # Second moment of area (m^4)

    def test_euler_buckling_pinned_column(self):
        """Test Euler buckling for pinned-pinned column."""
        result = self.column.euler_buckling(
            length=self.length,
            E=self.E,
            second_moment=self.second_moment,
            end_conditions="pinned",
            safety_factor=1.0,
        )

        # Verify return structure
        assert isinstance(result, dict)
        required_keys = [
            "critical_load",
            "design_load",
            "critical_stress",
            "effective_length",
            "K_factor",
            "slenderness_ratio",
            "radius_of_gyration",
            "recommendation",
        ]
        for key in required_keys:
            assert key in result

        # Analytical verification for pinned column
        # P_cr = π²EI / L²
        expected_critical_load = (np.pi**2 * self.E * self.second_moment) / (
            self.length**2
        )

        critical_load = float(result["critical_load"])
        effective_length = float(result["effective_length"])
        design_load = float(result["design_load"])

        assert abs(critical_load - expected_critical_load) < 1e-6
        assert result["K_factor"] == 1.0
        assert abs(effective_length - self.length) < 1e-10
        assert abs(design_load - critical_load) < 1e-10  # safety_factor = 1.0

    def test_euler_buckling_fixed_column(self):
        """Test Euler buckling for fixed-fixed column."""
        result = self.column.euler_buckling(
            length=self.length,
            E=self.E,
            second_moment=self.second_moment,
            end_conditions="fixed",
            safety_factor=2.0,
        )

        # Fixed-fixed column has K = 0.5
        expected_effective_length = 0.5 * self.length
        expected_critical_load = (np.pi**2 * self.E * self.second_moment) / (
            expected_effective_length**2
        )

        assert result["K_factor"] == 0.5
        assert abs(result["effective_length"] - expected_effective_length) < 1e-10
        assert abs(result["critical_load"] - expected_critical_load) < 1e-6
        assert abs(result["design_load"] - expected_critical_load / 2.0) < 1e-6

    def test_euler_buckling_cantilever_column(self):
        """Test Euler buckling for fixed-free (cantilever) column."""
        result = self.column.euler_buckling(
            length=self.length,
            E=self.E,
            second_moment=self.second_moment,
            end_conditions="fixed_free",
            safety_factor=1.0,
        )

        # Cantilever column has K = 2.0
        expected_effective_length = 2.0 * self.length
        expected_critical_load = (np.pi**2 * self.E * self.second_moment) / (
            expected_effective_length**2
        )

        assert result["K_factor"] == 2.0
        assert abs(result["effective_length"] - expected_effective_length) < 1e-10
        assert abs(result["critical_load"] - expected_critical_load) < 1e-6

    def test_euler_buckling_fixed_pinned_column(self):
        """Test Euler buckling for fixed-pinned column."""
        result = self.column.euler_buckling(
            length=self.length,
            E=self.E,
            second_moment=self.second_moment,
            end_conditions="fixed_pinned",
            safety_factor=1.5,
        )

        # Fixed-pinned column has K = 0.7
        expected_effective_length = 0.7 * self.length
        expected_critical_load = (np.pi**2 * self.E * self.second_moment) / (
            expected_effective_length**2
        )

        assert result["K_factor"] == 0.7
        assert abs(result["effective_length"] - expected_effective_length) < 1e-10
        assert abs(result["critical_load"] - expected_critical_load) < 1e-6
        assert abs(result["design_load"] - expected_critical_load / 1.5) < 1e-6

    def test_euler_buckling_slenderness_recommendations(self):
        """Test slenderness ratio calculations and recommendations."""
        # Test short column (low slenderness)
        short_result = self.column.euler_buckling(
            length=1.0,  # Short column
            E=self.E,
            second_moment=1e-4,  # Large second moment
            end_conditions="pinned",
        )
        assert "Short column" in short_result["recommendation"]

        # Test very slender column (high slenderness)
        slender_result = self.column.euler_buckling(
            length=10.0,  # Long column
            E=self.E,
            second_moment=1e-8,  # Small second moment
            end_conditions="pinned",
        )
        assert "Very slender" in slender_result["recommendation"]

    def test_euler_buckling_analytical_verification(self):
        """Test against known analytical solution for standard case."""
        # Standard case: 4m pinned steel column
        length = 4.0  # m
        E = 200e9  # Pa
        second_moment = 1e-5  # m^4

        result = self.column.euler_buckling(
            length=length,
            E=E,
            second_moment=second_moment,
            end_conditions="pinned",
        )

        # Analytical solution: P_cr = π²EI/L²
        expected_critical_load = (np.pi**2 * E * second_moment) / (length**2)

        # Verify within 0.1% tolerance
        error = (
            abs(result["critical_load"] - expected_critical_load)
            / expected_critical_load
        )
        assert error < 0.001

    def test_euler_buckling_input_validation(self):
        """Test input validation for euler_buckling method."""
        # Test negative length
        with pytest.raises(ValueError, match="Length must be positive"):
            self.column.euler_buckling(
                length=-1.0,
                E=self.E,
                second_moment=self.second_moment,
            )

        # Test zero elastic modulus
        with pytest.raises(ValueError, match="Elastic modulus must be positive"):
            self.column.euler_buckling(
                length=self.length,
                E=0.0,
                second_moment=self.second_moment,
            )

        # Test negative second moment
        with pytest.raises(ValueError, match="Second moment of area must be positive"):
            self.column.euler_buckling(
                length=self.length,
                E=self.E,
                second_moment=-1e-6,
            )

        # Test negative safety factor
        with pytest.raises(ValueError, match="Safety factor must be positive"):
            self.column.euler_buckling(
                length=self.length,
                E=self.E,
                second_moment=self.second_moment,
                safety_factor=-1.0,
            )

    def test_euler_buckling_consistency(self):
        """Test consistency of calculations across different parameters."""
        base_result = self.column.euler_buckling(
            length=self.length,
            E=self.E,
            second_moment=self.second_moment,
            end_conditions="pinned",
        )

        # Double the length should quarter the critical load
        double_length_result = self.column.euler_buckling(
            length=2 * self.length,
            E=self.E,
            second_moment=self.second_moment,
            end_conditions="pinned",
        )

        expected_ratio = 4.0  # P_cr ∝ 1/L²
        actual_ratio = (
            base_result["critical_load"] / double_length_result["critical_load"]
        )
        assert abs(actual_ratio - expected_ratio) < 0.01

        # Double the second moment should double the critical load
        double_I_result = self.column.euler_buckling(
            length=self.length,
            E=self.E,
            second_moment=2 * self.second_moment,
            end_conditions="pinned",
        )

        expected_ratio = 2.0  # P_cr ∝ I
        actual_ratio = double_I_result["critical_load"] / base_result["critical_load"]
        assert abs(actual_ratio - expected_ratio) < 0.01

    def test_euler_buckling_safety_factor_application(self):
        """Test that safety factor is correctly applied."""
        safety_factors = [1.0, 1.5, 2.0, 3.0]

        for sf in safety_factors:
            result = self.column.euler_buckling(
                length=self.length,
                E=self.E,
                second_moment=self.second_moment,
                end_conditions="pinned",
                safety_factor=sf,
            )

            expected_design_load = result["critical_load"] / sf
            assert abs(result["design_load"] - expected_design_load) < 1e-10

    def test_euler_buckling_return_types(self):
        """Test that return types are correct."""
        result = self.column.euler_buckling(
            length=self.length,
            E=self.E,
            second_moment=self.second_moment,
        )

        # Check numeric values are floats
        numeric_keys = [
            "critical_load",
            "design_load",
            "critical_stress",
            "effective_length",
            "K_factor",
            "slenderness_ratio",
            "radius_of_gyration",
        ]

        for key in numeric_keys:
            # Get value and assert it's a numeric type
            assert key in result
            assert isinstance(result[key], (float, np.floating))

            # Use cast to help type checker understand the type
            numeric_value = cast(float, result[key])

            # Test for NaN and infinity
            if isinstance(result[key], np.floating):
                np_value = cast(np.floating, result[key])
                assert not np.isnan(np_value.item())
                assert not np.isinf(np_value.item())
            else:
                # It's a regular Python float
                assert not np.isnan(numeric_value)
                assert not np.isinf(numeric_value)

        # Check recommendation is string
        assert isinstance(result["recommendation"], str)
        assert len(result["recommendation"]) > 0

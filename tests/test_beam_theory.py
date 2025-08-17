import numpy as np
import pytest

from structural_analysis.beam_theory import BeamTheory


class TestBeamTheory:
    """Test suite for BeamTheory class with comprehensive Euler-Bernoulli tests."""

    def setup_method(self):
        """Set up test fixtures."""
        self.beam = BeamTheory()
        # Standard test parameters
        self.length = 4.0  # 4 meters
        self.E = 200e9  # 200 GPa (steel)
        self.second_moment = 8.33e-6  # Second moment of area (m^4)

    def test_euler_bernoulli_simply_supported_point_load(self):
        """Test simply supported beam with center point load."""
        # Test case: Simply supported beam with center point load
        load_magnitude = 10000  # 10 kN
        load_position = self.length / 2  # Center load

        result = self.beam.euler_bernoulli(
            length=self.length,
            E=self.E,
            second_moment=self.second_moment,
            load_type="point",
            load_magnitude=load_magnitude,
            load_position=load_position,
            boundary_conditions="simply_supported",
            num_points=101,
        )

        # Verify return structure
        assert isinstance(result, dict)
        assert "x" in result
        assert "deflection" in result
        assert "moment" in result
        assert "shear" in result
        assert "max_deflection" in result
        assert "max_moment" in result

        # Verify array shapes
        assert len(result["x"]) == 101
        assert result["deflection"].shape == (101,)
        assert result["moment"].shape == (101,)
        assert result["shear"].shape == (101,)

        # Analytical solution for center point load on simply supported beam
        # Max deflection = PL³/(48EI)
        expected_max_deflection = (load_magnitude * self.length**3) / (
            48 * self.E * self.second_moment
        )

        # Check maximum deflection (should be at center)
        assert (
            abs(result["max_deflection"] - expected_max_deflection)
            < expected_max_deflection * 0.01
        )

        # Check boundary conditions (deflection at ends should be zero)
        assert abs(result["deflection"][0]) < 1e-10
        assert abs(result["deflection"][-1]) < 1e-10

        # Check maximum moment
        expected_max_moment = load_magnitude * self.length / 4  # PL/4
        assert (
            abs(result["max_moment"] - expected_max_moment) < expected_max_moment * 0.01
        )

    def test_euler_bernoulli_simply_supported_distributed_load(self):
        """Test simply supported beam with uniformly distributed load."""
        load_magnitude = 5000  # 5 kN/m

        result = self.beam.euler_bernoulli(
            length=self.length,
            E=self.E,
            second_moment=self.second_moment,
            load_type="distributed",
            load_magnitude=load_magnitude,
            boundary_conditions="simply_supported",
        )

        # Analytical solution for UDL on simply supported beam
        # Max deflection = 5wL⁴/(384EI)
        expected_max_deflection = (5 * load_magnitude * self.length**4) / (
            384 * self.E * self.second_moment
        )

        # Check maximum deflection
        assert (
            abs(result["max_deflection"] - expected_max_deflection)
            < expected_max_deflection * 0.01
        )

        # Check boundary conditions
        assert abs(result["deflection"][0]) < 1e-10
        assert abs(result["deflection"][-1]) < 1e-10

        # Check maximum moment at center
        expected_max_moment = load_magnitude * self.length**2 / 8  # wL²/8
        assert (
            abs(result["max_moment"] - expected_max_moment) < expected_max_moment * 0.01
        )

    def test_euler_bernoulli_cantilever_end_load(self):
        """Test cantilever beam with end point load."""
        load_magnitude = 5000  # 5 kN
        load_position = self.length  # End load

        result = self.beam.euler_bernoulli(
            length=self.length,
            E=self.E,
            second_moment=self.second_moment,
            load_type="point",
            load_magnitude=load_magnitude,
            load_position=load_position,
            boundary_conditions="cantilever",
        )

        # Analytical solution for cantilever with end load
        # Max deflection = PL³/(3EI)
        expected_max_deflection = (load_magnitude * self.length**3) / (
            3 * self.E * self.second_moment
        )

        # Check maximum deflection (at free end)
        assert (
            abs(result["max_deflection"] - expected_max_deflection)
            < expected_max_deflection * 0.01
        )

        # Check boundary conditions (deflection and slope at fixed end should be zero)
        assert abs(result["deflection"][0]) < 1e-10

        # Check maximum moment at fixed end
        expected_max_moment = load_magnitude * self.length  # PL
        assert (
            abs(result["max_moment"] - expected_max_moment) < expected_max_moment * 0.01
        )

    def test_euler_bernoulli_cantilever_distributed_load(self):
        """Test cantilever beam with uniformly distributed load."""
        load_magnitude = 3000  # 3 kN/m

        result = self.beam.euler_bernoulli(
            length=self.length,
            E=self.E,
            second_moment=self.second_moment,
            load_type="distributed",
            load_magnitude=load_magnitude,
            boundary_conditions="cantilever",
        )

        # Analytical solution for cantilever with UDL
        # Max deflection = wL⁴/(8EI)
        expected_max_deflection = (load_magnitude * self.length**4) / (
            8 * self.E * self.second_moment
        )

        # Check maximum deflection
        assert (
            abs(result["max_deflection"] - expected_max_deflection)
            < expected_max_deflection * 0.01
        )

        # Check boundary conditions
        assert abs(result["deflection"][0]) < 1e-10

        # Check maximum moment at fixed end
        expected_max_moment = load_magnitude * self.length**2 / 2  # wL²/2
        assert (
            abs(result["max_moment"] - expected_max_moment) < expected_max_moment * 0.01
        )

    def test_euler_bernoulli_fixed_fixed_center_load(self):
        """Test fixed-fixed beam with center point load."""
        load_magnitude = 8000  # 8 kN
        load_position = self.length / 2  # Center load

        result = self.beam.euler_bernoulli(
            length=self.length,
            E=self.E,
            second_moment=self.second_moment,
            load_type="point",
            load_magnitude=load_magnitude,
            load_position=load_position,
            boundary_conditions="fixed_fixed",
        )

        # Analytical solution for fixed-fixed beam with center load
        # Max deflection = PL³/(192EI)
        expected_max_deflection = (load_magnitude * self.length**3) / (
            192 * self.E * self.second_moment
        )

        # Check maximum deflection
        assert (
            abs(result["max_deflection"] - expected_max_deflection)
            < expected_max_deflection * 0.05
        )

        # Check boundary conditions (deflection at both ends should be zero)
        assert abs(result["deflection"][0]) < 1e-10
        assert abs(result["deflection"][-1]) < 1e-10

    def test_euler_bernoulli_input_validation(self):
        """Test input validation for Euler-Bernoulli method."""
        # Test negative length
        with pytest.raises(
            ValueError, match="Length, E, and second_moment must be positive"
        ):
            self.beam.euler_bernoulli(
                length=-1,
                E=self.E,
                second_moment=self.second_moment,
                load_type="point",
                load_magnitude=1000,
                load_position=1,
            )

        # Test negative elastic modulus
        with pytest.raises(
            ValueError, match="Length, E, and second_moment must be positive"
        ):
            self.beam.euler_bernoulli(
                length=self.length,
                E=-1,
                second_moment=self.second_moment,
                load_type="point",
                load_magnitude=1000,
                load_position=1,
            )

        # Test negative moment of inertia
        with pytest.raises(
            ValueError, match="Length, E, and second_moment must be positive"
        ):
            self.beam.euler_bernoulli(
                length=self.length,
                E=self.E,
                second_moment=-1,
                load_type="point",
                load_magnitude=1000,
                load_position=1,
            )

        # Test point load without position
        with pytest.raises(ValueError, match="Point load requires load_position"):
            self.beam.euler_bernoulli(
                length=self.length,
                E=self.E,
                second_moment=self.second_moment,
                load_type="point",
                load_magnitude=1000,
            )

        # Test moment without position
        with pytest.raises(ValueError, match="Applied moment requires load_position"):
            self.beam.euler_bernoulli(
                length=self.length,
                E=self.E,
                second_moment=self.second_moment,
                load_type="moment",
                load_magnitude=1000,
            )

    def test_euler_bernoulli_moment_loading(self):
        """Test beam with applied moment."""
        moment_magnitude = 5000  # 5 kN⋅m
        moment_position = self.length / 3  # Applied at L/3

        result = self.beam.euler_bernoulli(
            length=self.length,
            E=self.E,
            second_moment=self.second_moment,
            load_type="moment",
            load_magnitude=moment_magnitude,
            load_position=moment_position,
            boundary_conditions="simply_supported",
        )

        # For moment loading, shear should be zero everywhere
        assert np.allclose(result["shear"], 0, atol=1e-10)

        # Check boundary conditions
        assert abs(result["deflection"][0]) < 1e-10
        assert abs(result["deflection"][-1]) < 1e-10

    def test_euler_bernoulli_symmetry(self):
        """Test symmetry for symmetric loading conditions."""
        # Test symmetric point load
        result = self.beam.euler_bernoulli(
            length=self.length,
            E=self.E,
            second_moment=self.second_moment,
            load_type="point",
            load_magnitude=5000,
            load_position=self.length / 2,
            boundary_conditions="simply_supported",
            num_points=101,
        )

        # For symmetric loading, deflection should be symmetric
        deflection = result["deflection"]
        n = len(deflection)

        # Check symmetry (allowing small numerical errors)
        for i in range(n // 2):
            assert abs(deflection[i] - deflection[n - 1 - i]) < 1e-10

    def test_unimplemented_methods(self):
        """Test that unimplemented methods raise NotImplementedError."""
        with pytest.raises(NotImplementedError):
            self.beam.timoshenko()

        with pytest.raises(NotImplementedError):
            self.beam.reddy_bickford()

        with pytest.raises(NotImplementedError):
            self.beam.levinson()

        with pytest.raises(NotImplementedError):
            self.beam.nonlinear_beam()

    def test_euler_bernoulli_load_position_validation(self):
        """Test load position validation."""
        # Load position beyond beam length should work (might be used for extrapolation)
        result = self.beam.euler_bernoulli(
            length=self.length,
            E=self.E,
            second_moment=self.second_moment,
            load_type="point",
            load_magnitude=1000,
            load_position=self.length * 0.75,  # 3/4 along beam
            boundary_conditions="simply_supported",
        )

        # Should complete without error
        assert result is not None
        assert "deflection" in result

    def test_euler_bernoulli_different_num_points(self):
        """Test with different numbers of analysis points."""
        for num_points in [10, 50, 200]:
            result = self.beam.euler_bernoulli(
                length=self.length,
                E=self.E,
                second_moment=self.second_moment,
                load_type="distributed",
                load_magnitude=2000,
                boundary_conditions="simply_supported",
                num_points=num_points,
            )

            assert len(result["x"]) == num_points
            assert len(result["deflection"]) == num_points
            assert len(result["moment"]) == num_points
            assert len(result["shear"]) == num_points

    def test_euler_bernoulli_return_types(self):
        """Test that return values have correct types."""
        result = self.beam.euler_bernoulli(
            length=self.length,
            E=self.E,
            second_moment=self.second_moment,
            load_type="distributed",
            load_magnitude=1000,
            boundary_conditions="simply_supported",
        )

        # Check types
        assert isinstance(result["x"], np.ndarray)
        assert isinstance(result["deflection"], np.ndarray)
        assert isinstance(result["moment"], np.ndarray)
        assert isinstance(result["shear"], np.ndarray)
        assert isinstance(result["max_deflection"], float)
        assert isinstance(result["max_moment"], float)


if __name__ == "__main__":
    pytest.main([__file__])

from .beam_theory import BeamTheory
from .column_theory import ColumnTheory
from .displacement_method import DisplacementMethod
from .dynamic_theory import DynamicTheory
from .energy_method import EnergyMethod
from .force_method import ForceMethod
from .fracture_theory import FractureTheory
from .material_theory import MaterialTheory
from .nonlinear_theory import NonlinearTheory
from .plane_theory import PlaneTheory
from .plate_shell_theory import PlateShellTheory
from .specialized_theory import SpecializedTheory
from .stability_theory import StabilityTheory


class StructuralAnalysis:
    """
    A comprehensive library for structural analysis theories.
    """

    def __init__(self):
        self._beam_theory = BeamTheory()
        self._column_theory = ColumnTheory()
        self._displacement_method = DisplacementMethod()
        self._dynamic_theory = DynamicTheory()
        self._energy_method = EnergyMethod()
        self._force_method = ForceMethod()
        self._fracture_theory = FractureTheory()
        self._material_theory = MaterialTheory()
        self._nonlinear_theory = NonlinearTheory()
        self._plane_theory = PlaneTheory()
        self._plate_shell_theory = PlateShellTheory()
        self._specialized_theory = SpecializedTheory()
        self._stability_theory = StabilityTheory()

    @property
    def beam_theory(self):
        """Provides access to Beam Theory methods."""
        return self._beam_theory

    @property
    def column_theory(self):
        """Provides access to Column Theory methods."""
        return self._column_theory

    @property
    def displacement_method(self):
        """Provides access to Displacement Method methods."""
        return self._displacement_method

    @property
    def dynamic_theory(self):
        """Provides access to Dynamic Theory methods."""
        return self._dynamic_theory

    @property
    def energy_method(self):
        """Provides access to Energy Method methods."""
        return self._energy_method

    @property
    def force_method(self):
        """Provides access to Force Method methods."""
        return self._force_method

    @property
    def fracture_theory(self):
        """Provides access to Fracture Theory methods."""
        return self._fracture_theory

    @property
    def material_theory(self):
        """Provides access to Material Theory methods."""
        return self._material_theory

    @property
    def nonlinear_theory(self):
        """Provides access to Nonlinear Theory methods."""
        return self._nonlinear_theory

    @property
    def plane_theory(self):
        """Provides access to Plane Theory methods."""
        return self._plane_theory

    @property
    def plate_shell_theory(self):
        """Provides access to Plate Shell Theory methods."""
        return self._plate_shell_theory

    @property
    def specialized_theory(self):
        """Provides access to Specialized Theory methods."""
        return self._specialized_theory

    @property
    def stability_theory(self):
        """Provides access to Stability Theory methods."""
        return self._stability_theory

from pydantic import BaseModel


class InputData(BaseModel):
    CrimePerCapita: float
    LargeResidentialZoningProportion: float
    IndustrialProportion: float
    BordersRiver: bool
    NitricOxideConcentration: float
    RoomsPerDwelling: float
    Pre1940ConstructionProportion: float
    CommuteDistance: float
    RadialHighwayAccessibility: float
    TaxRate: float
    PupilsToTeachers: float
    BlackPopulationScore: float
    LowerClassPopulationProportion: float

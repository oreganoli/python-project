import pandas as pd
from sklearn.linear_model import LinearRegression


def make_model():
    data = pd.read_csv("data/housing.csv", sep="\ +", engine="python")
    data.columns = [
        "PerCapitaCrimeRate",
        "LargeResidentialZoningProportion",
        "IndustrialProportion",
        "BordersRiver",
        "NitricOxideConcentration",
        "RoomsPerDwelling",
        "Pre1940ConstructionProportion",
        "CommuteDistance",
        "RadialHighwayAccessibility",
        "TaxRate",
        "PupilsToTeachers",
        "BlackPopulationScore",
        "LowerClassPopulationProportion",
        "MedianValueInThousands"
    ]
    # Split dataset into inputs and output
    X = data[[
        "PerCapitaCrimeRate",
        "LargeResidentialZoningProportion",
        "IndustrialProportion",
        "BordersRiver",
        "NitricOxideConcentration",
        "RoomsPerDwelling",
        "Pre1940ConstructionProportion",
        "CommuteDistance",
        "RadialHighwayAccessibility",
        "TaxRate",
        "PupilsToTeachers",
        "BlackPopulationScore",
        "LowerClassPopulationProportion",
    ]]
    y = data["MedianValueInThousands"]
    # Train model
    model = LinearRegression()
    model.fit(X, y)

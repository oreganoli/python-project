import pandas as pd

if __name__ == "__main__":
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
    print(data)

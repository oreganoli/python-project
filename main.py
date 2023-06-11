import model
from fastapi import FastAPI
from domain import InputData

model = model.make_model()
app = FastAPI()


@app.post("/price/predict")
def predict_price(data: InputData):
    value = model.predict([[
        data.CrimePerCapita,
        data.LargeResidentialZoningProportion,
        data.IndustrialProportion,
        1.0 if data.BordersRiver else 0.0,
        data.NitricOxideConcentration,
        data.RoomsPerDwelling,
        data.Pre1940ConstructionProportion,
        data.CommuteDistance,
        data.RadialHighwayAccessibility,
        data.TaxRate,
        data.PupilsToTeachers,
        data.BlackPopulationScore,
        data.LowerClassPopulationProportion
    ]])
    return value[0]

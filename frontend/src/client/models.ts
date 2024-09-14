export type MeasurementBase = {
    soil_moisture: number;
    air_humidity: number;
    pressure: number;
    temperature: number;
    uv_index: number;
}


export type MeasurementPublic = MeasurementBase & {id: number; timestamp: string}


export type MeasurementsPublic = {
	data: Array<MeasurementPublic>;
	count: number;
}


export type PlantWatered = {
	watered: boolean;
	message: string;
	moisture: number;
}


export enum MeasurementUnit {
	SoilMoisture = '%',
	AirHumidity = '%',
	Pressure = 'hPa',
	Temperature = '\u00B0C',
	UVIndex = ''
}
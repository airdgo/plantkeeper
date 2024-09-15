import type { CancelablePromise } from './core/CancelablePromise';
import { OpenAPI } from './core/OpenAPI';
import { request as __request } from './core/request';

import type { MeasurementsPublic, MeasurementBase, PlantWatered } from './models';


export type TDataReadMeasurements = {
	start_date: Date
	end_date: Date
	limit?: number
	skip?: number
}

export class MeasurementsService {

	/**
	 * Read Measurements
	 * Retrieve Measurements
	 * @returns MeasurementsPublic Successful Response
	 * @throws ApiError
	 */
	public static readMeasurements(data: TDataReadMeasurements): CancelablePromise<MeasurementsPublic> {
		const { start_date = new Date(), end_date = new Date(), limit = 100, skip = 0 } = data;
		const isoDateTime = (date: Date) => new Date(date.getTime() - (date.getTimezoneOffset() * 60000)).toISOString();

		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/measurements/',
			query: {
				start_date: isoDateTime(start_date), end_date: isoDateTime(end_date), skip, limit
			},
			errors: {
				422: `Validation Error`,
			},
		});
	}


	/**
	 * Make a New Measurement
	 * @returns MeasurementBase Successful Response
	 * @throws ApiError
	 */
	public static makeMeasurement(): CancelablePromise<MeasurementBase> {
		return __request(OpenAPI, {
			method: 'GET',
			url: '/api/v1/measurements/now',
			errors: {
				422: `Validation Error`,
			},
		});
	}
}

export class WateringService {
	/**
	 * Water the plant
	 * @returns Plant Watered Successful Response Message
	 * @throws ApiError
	 */
	public static waterThePlant(): CancelablePromise<PlantWatered> {
		return __request(OpenAPI, {
			method: 'POST',
			url: '/api/v1/watering/water-plant',
			errors: {
				422: `Validation Error`,
			},
		});
	}
}
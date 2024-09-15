import {
  Area,
  AreaChart,
  CartesianGrid,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts"
import type { AxisDomain } from "recharts/types/util/types"
import {
  type MeasurementBase,
  MeasurementUnit,
  type MeasurementsPublic,
} from "../../client"

type Series = {
  [key: string]: {
    data: SingleMeasurement[]
    unit: MeasurementUnit
    yUpperLimit?: number
  }
}

type SingleMeasurement = {
  date: string
  measurement: string
}

const MeasurementChart = ({
  measurementType,
  measurements,
}: { measurementType: string; measurements: MeasurementsPublic }) => {
  const getMeasurement = (type: keyof MeasurementBase): SingleMeasurement[] =>
    measurements.data.map((measurement) => ({
      date: measurement.timestamp,
      measurement: measurement[type].toFixed(2),
    }))

  const series: Series = {
    "Soil Moisture": {
      data: getMeasurement("soil_moisture"),
      unit: MeasurementUnit.SoilMoisture,
      yUpperLimit: 110,
    },
    "Air Humidity": {
      data: getMeasurement("air_humidity"),
      unit: MeasurementUnit.AirHumidity,
    },
    Pressure: {
      data: getMeasurement("pressure"),
      unit: MeasurementUnit.Pressure,
      yUpperLimit: 1100,
    },
    Temperature: {
      data: getMeasurement("temperature"),
      unit: MeasurementUnit.Temperature,
    },
    "UV Index": {
      data: getMeasurement("uv_index"),
      unit: MeasurementUnit.UVIndex,
    },
  }

  const measurement = series[measurementType]
  const measurementUnit = measurement.unit

  const yAxisLabel = measurementUnit
    ? `${measurementType} [${measurementUnit}]`
    : measurementType
  const yAxisDomain: AxisDomain = [
    0,
    series[measurementType]?.yUpperLimit ?? "auto",
  ]

  return (
    <ResponsiveContainer width={"100%"} height={300}>
      <AreaChart data={measurement.data}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="date" angle={0} tick={false} label="Time" />
        <YAxis
          type="number"
          domain={yAxisDomain}
          label={{ value: yAxisLabel, angle: -90, position: "insideLeft" }}
        />
        <Tooltip />
        <Area
          type="monotone"
          dataKey="measurement"
          strokeWidth={1.5}
          stroke="#006D92"
          fill="#006d92cc"
        />
      </AreaChart>
    </ResponsiveContainer>
  )
}

export default MeasurementChart

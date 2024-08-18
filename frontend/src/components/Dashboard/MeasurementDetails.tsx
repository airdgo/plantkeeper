import { Box, Icon, VStack } from "@chakra-ui/react"
import {
  FaCloudRain,
  FaSun,
  FaTachometerAlt,
  FaTemperatureHigh,
  FaTint,
} from "react-icons/fa"
import { type MeasurementBase, MeasurementUnit } from "../../client"

const MeasurementDetails = ({ data }: { data?: MeasurementBase }) => {
  return (
    <VStack spacing={4} align="flex-start">
      <Box>
        <Icon as={FaTint} mr={2} color="blue.400" />
        Soil Moisture:{" "}
        {data?.soil_moisture.toFixed(2) + MeasurementUnit.SoilMoisture}
      </Box>
      <Box>
        <Icon as={FaCloudRain} mr={2} color="teal.400" />
        Air Humidity:{" "}
        {data?.air_humidity.toFixed(2) + MeasurementUnit.AirHumidity}
      </Box>
      <Box>
        <Icon as={FaTemperatureHigh} mr={2} color="orange.400" />
        Temperature: {data?.temperature + MeasurementUnit.Temperature}
      </Box>
      <Box>
        <Icon as={FaTachometerAlt} mr={2} color="purple.400" />
        Pressure: {Math.trunc(data?.pressure ?? 0) + MeasurementUnit.Pressure}
      </Box>
      <Box>
        <Icon as={FaSun} mr={2} color="yellow.400" />
        UV Index: {Math.trunc(data?.uv_index ?? 0) + MeasurementUnit.UVIndex}
      </Box>
    </VStack>
  )
}

export default MeasurementDetails

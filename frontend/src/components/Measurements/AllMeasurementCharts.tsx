import { Heading, SimpleGrid } from "@chakra-ui/react"
import { useSuspenseQuery } from "@tanstack/react-query"
import type { DateRange } from "react-day-picker"
import { MeasurementsService } from "../../client"
import MeasurementChart from "./MeasurementChart"
import NoAvailableData from "./NoAvailableData"

const AllMeasurementCharts = ({ dateRange }: { dateRange: DateRange }) => {
  const { data: measurements } = useSuspenseQuery({
    queryKey: ["measurements", dateRange.from, dateRange.to],
    queryFn: () =>
      MeasurementsService.readMeasurements({
        start_date: dateRange.from!,
        end_date: dateRange.to!,
      }),
  })
  const measurementTypes = [
    "Soil Moisture",
    "Air Humidity",
    "Pressure",
    "Temperature",
    "UV Index",
  ]

  return measurements.count > 0 ? (
    <SimpleGrid columns={2} spacingY={"3rem"} spacingX={"4rem"} my={10}>
      {measurementTypes.map((type) => (
        <div key={type}>
          <Heading size="md" textAlign={{ base: "center" }} pb={5}>
            {type}
          </Heading>
          <MeasurementChart
            key={type}
            measurementType={type}
            measurements={measurements}
          />
        </div>
      ))}
    </SimpleGrid>
  ) : (
    <NoAvailableData />
  )
}

export default AllMeasurementCharts

import { Container, Heading, Spinner } from "@chakra-ui/react"
import { createFileRoute } from "@tanstack/react-router"
import { Suspense, useState } from "react"
import type { DateRange } from "react-day-picker"
import AllMeasurementCharts from "../../components/Measurements/AllMeasurementCharts"
import RangeDatePicker from "../../components/Measurements/RangeDatePicker"
import { endOfDay, startOfDay } from "../../utils"

export const Route = createFileRoute("/_layout/measurements")({
  component: Measurements,
})

function Measurements() {
  const [selectedDateRange, setSelectedDateRange] = useState<DateRange>({
    from: startOfDay(new Date()),
    to: endOfDay(new Date()),
  })

  return (
    <Container maxW="full" display="flex" flexDir="column">
      <Heading size="lg" textAlign={{ base: "center", md: "left" }} pt={12}>
        Measurements
      </Heading>

      <RangeDatePicker
        dateRange={selectedDateRange}
        setDateRange={setSelectedDateRange}
      />

      <Suspense fallback={<Spinner />}>
        <AllMeasurementCharts dateRange={selectedDateRange} />
      </Suspense>
    </Container>
  )
}

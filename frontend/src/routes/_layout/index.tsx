import { Box, Container, Flex, Text } from "@chakra-ui/react"
import { useQuery, useQueryClient } from "@tanstack/react-query"
import { createFileRoute } from "@tanstack/react-router"
import { useEffect, useState } from "react"
import { MeasurementsService, type UserPublic } from "../../client"
import MeasurementDetails from "../../components/Dashboard/MeasurementDetails"
import SoilMoistureIndicator from "../../components/Dashboard/SoilMoistureIndixator"

export const Route = createFileRoute("/_layout/")({
  component: Dashboard,
})

function Dashboard() {
  const queryClient = useQueryClient()

  const currentUser = queryClient.getQueryData<UserPublic>(["currentUser"])

  const { data } = useQuery({
    queryKey: ["measurement"],
    queryFn: () => MeasurementsService.makeMeasurement(),
    refetchInterval: 60000,
  })

  const soilMoistureValue: number = Math.trunc(data?.soil_moisture || 0)
  const [soilMoistureColor, setSoilMoistureColor] = useState("white.400")

  useEffect(() => {
    if (soilMoistureValue < 30) setSoilMoistureColor("red.400")
    if (soilMoistureValue >= 30 && soilMoistureValue < 60)
      setSoilMoistureColor("orange.400")
    if (soilMoistureValue >= 60) setSoilMoistureColor("green.400")
  }, [soilMoistureValue])

  return (
    <>
      <Container maxW="full">
        <Box pt={12} m={4}>
          <Text fontSize="2xl">
            Hi, {currentUser?.full_name || currentUser?.email} 👋🏼
          </Text>
          <Text>Welcome back, nice to see you again!</Text>
        </Box>

        <Flex
          direction={{ base: "column", md: "row" }}
          justifyContent="space-around"
          alignItems="center"
          pt={12}
        >
          <MeasurementDetails data={data} />
          <SoilMoistureIndicator
            value={soilMoistureValue}
            color={soilMoistureColor}
          />
        </Flex>
      </Container>
    </>
  )
}

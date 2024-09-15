import {
  Button,
  CircularProgress,
  CircularProgressLabel,
  Text,
  VStack,
} from "@chakra-ui/react"
import { useMutation, useQueryClient } from "@tanstack/react-query"
import { type ApiError, WateringService } from "../../client"
import useCustomToast from "../../hooks/useCustomToast"

const SoilMoistureIndicator = ({
  value,
  color,
}: { value: number; color: string }) => {
  const queryClient = useQueryClient()
  const showToast = useCustomToast()

  const mutation = useMutation({
    mutationFn: () => WateringService.waterThePlant(),
    onSuccess: ({ watered, message }) => {
      watered
        ? showToast("Success!", message, "success")
        : showToast("Enough Water!", message, "error")
      watered && queryClient.invalidateQueries({ queryKey: ["measurement"] })
    },
    onError: (err: ApiError) => {
      const errDetail = (err.body as any)?.detail
      showToast("Something went wrong.", `${errDetail}`, "error")
    },
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["watering"] })
    },
  })

  const onSubmit = () => mutation.mutate()

  return (
    <VStack spacing={4}>
      <Text fontSize="2xl" as="b">
        Soil Moisture
      </Text>
      <CircularProgress value={value} size="20rem" color={color}>
        <CircularProgressLabel>{value}%</CircularProgressLabel>
      </CircularProgress>
      <Button
        isLoading={mutation.isPending}
        loadingText="Watering"
        colorScheme="teal"
        onClick={onSubmit}
      >
        Water the plant!
      </Button>
    </VStack>
  )
}

export default SoilMoistureIndicator

import { Flex, Icon, Text, VStack } from "@chakra-ui/react"
import { FaExclamationTriangle } from "react-icons/fa"

const NoAvailableData = () => {
  return (
    <Flex
      flex="1"
      alignItems="center"
      justifyContent="center"
      textAlign="center"
      py={10}
      px={6}
    >
      <VStack spacing={4}>
        <Icon as={FaExclamationTriangle} boxSize={12} color="orange.400" />
        <Text fontSize="lg" fontWeight="bold">
          No Data Available
        </Text>
        <Text fontSize="md" color="gray.500">
          There is no data for the selected period. Please try selecting a
          different date range.
        </Text>
      </VStack>
    </Flex>
  )
}

export default NoAvailableData

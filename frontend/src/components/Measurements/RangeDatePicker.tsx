import {
  HStack,
  IconButton,
  Popover,
  PopoverBody,
  PopoverContent,
  PopoverTrigger,
  Text,
} from "@chakra-ui/react"
import { type Dispatch, type SetStateAction, useState } from "react"
import { type DateRange, DayPicker } from "react-day-picker"
import { FaCalendar } from "react-icons/fa"
import { endOfDay, startOfDay } from "../../utils"

const RangeDatePicker = ({
  dateRange: selected,
  setDateRange: setSelected,
}: {
  dateRange: DateRange
  setDateRange: Dispatch<SetStateAction<DateRange>>
}) => {
  const formatDate = (date?: Date) =>
    date?.toLocaleDateString() || "Not selected"

  const [temporarySelected, setTemporarySelected] = useState<DateRange>({
    from: startOfDay(new Date()),
    to: endOfDay(new Date()),
  })

  const handleDateChange = (selectedRange: DateRange) => {
    setTemporarySelected(selectedRange)
  }
  const handlePopoverClose = () => {
    const { from, to } = temporarySelected
    setSelected({ from: startOfDay(from!), to: endOfDay(to!) })
  }

  return (
    <HStack spacing={5}>
      <Text>Start Date: {formatDate(selected.from)}</Text>
      <Text>End Date: {formatDate(selected.to)}</Text>
      <Popover onClose={handlePopoverClose}>
        <PopoverTrigger>
          <IconButton aria-label="Pick a date" icon={<FaCalendar />} />
        </PopoverTrigger>
        <PopoverContent width="min-content">
          <PopoverBody>
            <DayPicker
              mode="range"
              required={true}
              selected={selected}
              onSelect={handleDateChange}
            />
          </PopoverBody>
        </PopoverContent>
      </Popover>
    </HStack>
  )
}

export default RangeDatePicker

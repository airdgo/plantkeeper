export const startOfDay = (date: Date) => new Date(date.setHours(0, 0, 0, 0))
export const endOfDay = (date: Date) => new Date(date.setHours(23, 59, 59, 999))

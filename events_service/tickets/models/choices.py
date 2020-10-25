from enum import Enum


class TicketTypeSeatStatus(Enum):
    # Seat status change
    # available -> reserved -> booked -> available
    # available -> reserved -> available
    AVAILABLE = "Available"
    RESERVED = "Reserved"
    BOOKED = "Booked"


class SeatState(Enum):
    GOOD = "Good"
    WEARY = "Weary"
    BROKEN = "Broken"


class BookingStatus(Enum):
    # Booking status change
    # pending -> confirmed -> cancelled
    # pending -> timeout
    PENDING = "Pending"
    TIMEDOUT = "Timedout"
    CONFIRMED = "Confirmed"
    CANCELLED = "Cancelled"

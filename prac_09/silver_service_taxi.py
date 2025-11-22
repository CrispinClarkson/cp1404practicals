from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent a silver service taxi."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a silver service taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness

    def get_fare(self):
        """Get the current fare."""
        fare = self.flagfall + super().get_fare()
        return round(fare, 1)

    def __str__(self):
        """Return a string representation of the taxi."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

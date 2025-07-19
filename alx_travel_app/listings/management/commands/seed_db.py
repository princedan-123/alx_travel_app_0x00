"""A seeding script to populate the database."""
from listings.models import Status, Listing, Booking, Review

# create an instance of Listing
listing = Listing.objects.create(
    name='Felix_home', description='A spacious 3 bedroom apartment',
    location='Lagos Nigeria',
    price_per_night=1000.00
    )
booking = Booking.objects.create(
    listing=listing, start_date=,
    end_date=, total_price=1000.00
    status='Confirmed',
)
booking_id = models.UUIDField(default=uuid4, primary_key=True)
    listing = models.OneToOneField('Listing', on_delete=models.CASCADE, related_name='booking', null=False, blank=False)
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    status = models.CharField(null=False, blank=False, choices=Status.choices)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

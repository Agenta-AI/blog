from novu.config import NovuConfig
from novu.api import EventApi
from novu.api.subscriber import SubscriberApi
from novu.dto.subscriber import SubscriberDto

NOVU_API_KEY = ""
WEBHOOK_URL = ""
NovuConfig().configure("https://api.novu.co", NOVU_API_KEY)


def send_message(msg):
    your_subscriber_id = "123"  # Replace this with a unique user ID.

    # Define a subscriber instance
    subscriber = SubscriberDto(
        subscriber_id=your_subscriber_id,
        email="abc@gmail.com",
        first_name="John",
        last_name="Doe"
    )

    SubscriberApi().create(subscriber)
    SubscriberApi().credentials(subscriber_id=your_subscriber_id,
                                provider_id="discord",
                                webhook_url=WEBHOOK_URL)

    EventApi().trigger(
        name="discordworkflow",  # The trigger ID of the workflow.
        recipients=your_subscriber_id,
        payload={"content": msg},  # The payload of the event. It will be passed to the workflow.
    )

import os

from src.config import settings

IMAGE_BASE_PATH = os.path.join("public", "static", "images")


class LinkService:
    def get_image_anomalies_link(self, media_name: str, image: str):
        return os.path.join(IMAGE_BASE_PATH, media_name, "anomalies", f"{image}.png")

    def get_image_wonders_link(self, media_name: str, image: str):
        return os.path.join(IMAGE_BASE_PATH, media_name, "wonders", f"{image}.png")

    def get_image_faction_description_link(
        self, media_name: str, image_name: str, faction_id: str
    ):
        return os.path.join(
            IMAGE_BASE_PATH,
            media_name,
            "faction_description",
            f"faction-{image_name}-{faction_id}.png",
        )

    def get_restful_link(self, link_name: str | None):
        base_url = settings.env_base_link
        return f"{base_url}/endless/{link_name}"

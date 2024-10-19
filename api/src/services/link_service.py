import os

IMAGE_BASE_PATH = os.path.join("public", "static", "image")


class LinkService:
    def get_image_anomalies_link(self, media_name: str, image: str):
        return os.path.join(IMAGE_BASE_PATH, media_name, "anomalies", f"{image}.png")

    def get_image_wonders_link(self, media_name: str, image: str):
        return os.path.join(IMAGE_BASE_PATH, media_name, "wonders", f"{image}.png")

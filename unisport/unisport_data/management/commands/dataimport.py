from typing import Dict

import httpx
import structlog
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError, transaction

from unisport.unisport_data import json, models
from unisport.unisport_data.management.commands import errors

logger = structlog.get_logger(__name__)


class Command(BaseCommand):
    help = "Import unisport data"

    def handle(self, *args, **options) -> None:
        self._run()

    def _run(self) -> None:
        if not (import_url := settings.UNISPORT_SETTINGS.get("data_import_url")):
            raise CommandError(errors.MISSING_IMPORT_URL_FAIL)

        response = self._download_data(import_url)

        try:
            with transaction.atomic():
                self._save_currencies()
                self._save_data(response.json())
        except IntegrityError as ie:
            logger.error("Database import failure", exc=ie)
            raise CommandError(errors.DATABASE_IMPORT_FAIL)

        self.stdout.write(self.style.SUCCESS(f"Data imported from {import_url}"))

    def _download_data(self, import_url: str) -> httpx.Response:
        try:
            response = httpx.get(import_url, timeout=5)
            response.raise_for_status()

            return response
        except httpx.RequestError as re:
            logger.error("Data download request failed", url=re.request.url)
            raise CommandError(errors.DATA_DOWNLOAD_FAIL)
        except httpx.HTTPStatusError as se:
            logger.error(
                "Data download failed",
                status=se.response.status_code,
                response=se.response.text,
            )
            raise CommandError(errors.NETWORK_REQUEST_FAIL)

    def _save_data(self, data: Dict) -> None:
        data = json.UnisportProducts(**data)

        for product in data.products:
            product_db = json.create_product_from_json(product)
            product_db.save()

    def _save_currencies(self) -> None:
        models.Currency.objects.create(id="DKK", description="Danish Krone")
        models.Currency.objects.create(id="NOK", description="Norwegian Krone")
        models.Currency.objects.create(id="SEK", description="Swedish Krona")
        models.Currency.objects.create(id="GBP", description="British Pound")
        models.Currency.objects.create(id="EUR", description="Euro")

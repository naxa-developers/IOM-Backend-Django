from django.core.management.base import BaseCommand

import pandas as pd

from core.models import AvailableFacility

from django.contrib.gis.geos import Point


class Command(BaseCommand):
    help = 'load province data from province.xlsx file'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        df = pd.read_csv(path)
        upper_range = len(df)

        print("Wait Data is being Loaded")

        try:
            facility = [
                AvailableFacility(
                    name=df['Name'][row],
                    opening_hours=df['Opening hours'][row],
                    phone_number=df['Phone contact'][row],
                    email=df['Email Address'][row],
                    comments=df['Comments'][row],
                    type='place of worship',
                    location=Point(float(df['Long(X)'][row]), df['Lat(Y)'][row])

                ) for row in range(0, upper_range)

            ]

            available_data = AvailableFacility.objects.bulk_create(facility)

            if available_data:
                self.stdout.write('Successfully  updated data ..')

        except Exception as e:
            print(e)

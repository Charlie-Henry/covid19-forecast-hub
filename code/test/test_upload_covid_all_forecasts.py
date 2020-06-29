import unittest
from unittest.mock import patch, MagicMock

from zoltpy.connection import Project

from code.zoltar_scripts.upload_covid19_forecasts_to_zoltar import upload_covid_all_forecasts


class UploadCovidAllForecastsTestCase(unittest.TestCase):
    def test_upload_covid_all_forecasts(self):
        # has_changed: True | False
        # util.authenticate
        # conn.projects
        # project.name
        # model.abbreviation
        # model.edit
        # project.create_model
        connection_mock = MagicMock()
        project_mock = MagicMock()
        project_mock.name = 'COVID-19 Forecasts'
        tz1 = MagicMock()
        tz1.timezero_date = '2020-06-15'
        tz2 = MagicMock()
        tz2.timezero_date = '2020-06-22'
        project_mock.timezeros = [tz1, tz2]
        model1 = MagicMock()
        model1.abbreviation = 'COVIDhub-ensemble'
        model2 = MagicMock()
        model2.abbreviation = 'mobility'
        project_mock.models = [model1, model2]
        with patch('zoltpy.util.authenticate') as auth_mock:
            auth_mock.return_value = connection_mock
            connection_mock.projects = [project_mock]
            pass
        # Case: has_changed =False

        with patch('code.zoltar_scripts.upload_covid19_forecasts_to_zoltar.has_changed',
                   return_value=False), \
             patch('code.zoltar_scripts.upload_covid19_forecasts_to_zoltar.upload_forecasts',
                   return_value="Pass"):
            val_errors_or_pass = upload_covid_all_forecasts(
                'code/test/data/COVIDhub-ensemble/',
                'COVIDhub-ensemble')
        # Case: has_changed =True

        self.assertEqual("Pass", val_errors_or_pass)

# class MockConnection:
#
#     def projects(self):
#         pass
#
#
# class MockProject(Project):
#
#     def create_model

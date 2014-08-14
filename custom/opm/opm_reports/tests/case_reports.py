from collections import defaultdict
from datetime import datetime, date
from unittest import TestCase

from jsonobject import (JsonObject, DictProperty, DateTimeProperty,
    StringProperty, IntegerProperty, BooleanProperty)

from casexml.apps.case.models import CommCareCase
from custom.opm.opm_reports.reports import SharedDataProvider
from dimagi.utils.dates import DateSpan, add_months

from ..beneficiary import OPMCaseRow


class AggressiveDefaultDict(defaultdict):

    def __contains__(self, item):
        return True

class MockDataProvider(SharedDataProvider):
    """
    Mock data provider to manually specify vhnd availability per user
    """
    def __init__(self, datespan, vhnd_map=None):
        super(MockDataProvider, self).__init__(datespan)
        self.vhnd_map = vhnd_map if vhnd_map is not None else AggressiveDefaultDict(lambda: True)

    @property
    def vhnd_availability(self):
        return self.vhnd_map


class Report(JsonObject):
    month = IntegerProperty(required=True)
    year = IntegerProperty(required=True)
    block = StringProperty(required=True)

    _data_provider = None
    @property
    def data_provider(self):
        return self._data_provider

    @property
    def datespan(self):
        return DateSpan.from_month(self.month, self.year, inclusive=True)


class Form(JsonObject):
    xmlns = StringProperty('something')
    form = DictProperty(required=True)
    received_on = DateTimeProperty(required=True)


class OPMCase(CommCareCase):
    opened_on = DateTimeProperty(datetime(2010, 1, 1))
    block_name = StringProperty("Sahora")
    type = StringProperty("pregnancy")
    closed = BooleanProperty(default=False)
    closed_on = DateTimeProperty()
    awc_name = StringProperty("Atri")
    owner_id = StringProperty("Sahora")

    def __init__(self, forms=None, **kwargs):
        super(OPMCase, self).__init__(**kwargs)
        self._fake_forms = forms if forms is not None else []

    def get_forms(self):
        return self._fake_forms


class MockCaseRow(OPMCaseRow):
    """
    Spoof the following fields to create example cases
    """
    def __init__(self, case, report, data_provider=None):
        self.case = case
        self.report = report
        self.report.snapshot = None
        self.report.is_rendered_as_email = None
        self.report._data_provider = data_provider or MockDataProvider(self.report.datespan)
        super(MockCaseRow, self).__init__(case, report)


class OPMCaseReportTestBase(TestCase):

    def setUp(self):
        self.report_date = date(2014, 6, 1)
        self.report_datetime = datetime(2014, 6, 1)
        self.report = Report(month=6, year=2014, block="Atri")


def get_relative_edd_from_preg_month(report_date, month):
    months_until_edd = 10 - month
    new_year, new_month = add_months(report_date.year, report_date.month, months_until_edd)
    return type(report_date)(new_year, new_month, 1)


class MockDataTest(OPMCaseReportTestBase):

    def test_mock_data(self):
        report = Report(month=6, year=2014, block="Atri")
        form = Form(form={'foo': 'bar'}, received_on=datetime(2014, 6, 15))
        case = OPMCase(
            forms=[form],
            # add/override any desired case properties here
            edd=date(2014, 12, 10),
        )
        row = MockCaseRow(case, report)

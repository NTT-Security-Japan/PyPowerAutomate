
from typing import Dict
from .base import BaseAction


class Outlook365SendAnEmailV2(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_office365",
        "connectionName": "shared_office365",
        "operationId": "SendEmailV2"
    }

    def __init__(self, name: str, to: str, subject: str, body: str, importance: str):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.to: str = to
        self.subject: str = subject
        self.body: str = body
        self.importance: str = importance

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["emailMessage/To"] = self.to
        parameters["emailMessage/Subject"] = self.subject
        parameters["emailMessage/Body"] = self.body
        parameters["emailMessage/Importance"] = self.importance

        inputs["host"] = Outlook365SendAnEmailV2.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class Outlook365DeleteEmailV2(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_office365",
        "connectionName": "shared_office365",
        "operationId": "DeleteEmail_V2"
    }

    def __init__(self, name: str, messageid: str):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.messageid: str = messageid

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["messageId"] = self.messageid

        inputs["host"] = Outlook365DeleteEmailV2.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class Outlook365ExportEmailV2(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_office365",
        "connectionName": "shared_office365",
        "operationId": "ExportEmail_V2"
    }

    def __init__(self, name: str, messageid: str):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.messageid: str = messageid

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["messageId"] = self.messageid

        inputs["host"] = Outlook365ExportEmailV2.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class Outlook365FindMeetingTimesV2(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_office365",
        "connectionName": "shared_office365",
        "operationId": "FindMeetingTimes_V2"
    }

    def __init__(self, name: str, activitydomain: str):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.activitydomain: str = activitydomain

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["body/ActivityDomain"] = self.activitydomain

        inputs["host"] = Outlook365FindMeetingTimesV2.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class Outlook365FlagEmailV2(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_office365",
        "connectionName": "shared_office365",
        "operationId": "Flag_V2"
    }

    def __init__(self, name: str, messageid: str, flagstatus: str):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.messageid: str = messageid
        self.flagstatus: str = flagstatus

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["messageId"] = self.messageid
        parameters["body/flag/flagStatus"] = self.flagstatus

        inputs["host"] = Outlook365FlagEmailV2.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class Outlook365ForwardAnEmailV2(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_office365",
        "connectionName": "shared_office365",
        "operationId": "ForwardEmail_V2"
    }

    def __init__(self, name: str, message_id: str, torecipients: str):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.message_id: str = message_id
        self.torecipients: str = torecipients

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["message_id"] = self.message_id
        parameters["body/ToRecipients"] = self.torecipients

        inputs["host"] = Outlook365ForwardAnEmailV2.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class Outlook365GetAttachmentV2(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_office365",
        "connectionName": "shared_office365",
        "operationId": "GetAttachment_V2"
    }

    def __init__(self, name: str, messageid: str, attachmentid: str):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.messageid: str = messageid
        self.attachmentid: str = attachmentid

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["messageId"] = self.messageid
        parameters["attachmentId"] = self.attachmentid

        inputs["host"] = Outlook365GetAttachmentV2.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class Outlook365GetCalendarViewOfEventsV3(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_office365",
        "connectionName": "shared_office365",
        "operationId": "GetEventsCalendarViewV3"
    }

    def __init__(self, name: str, calendarid: str, startdatetimeutc: str, enddatetimeutc: str):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.calendarid: str = calendarid
        self.startdatetimeutc: str = startdatetimeutc
        self.enddatetimeutc: str = enddatetimeutc

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["calendarId"] = self.calendarid
        parameters["startDateTimeUtc"] = self.startdatetimeutc
        parameters["endDateTimeUtc"] = self.enddatetimeutc

        inputs["host"] = Outlook365GetCalendarViewOfEventsV3.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class Outlook365GetCalendarsV2(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_office365",
        "connectionName": "shared_office365",
        "operationId": "CalendarGetTables_V2"
    }

    def __init__(self, name: str):
        super().__init__(name)
        self.type = "OpenApiConnection"

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        inputs["host"] = Outlook365GetCalendarsV2.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class Outlook365GetEmailV2(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_office365",
        "connectionName": "shared_office365",
        "operationId": "GetEmailV2"
    }

    def __init__(self, name: str, messageid: str, includeattachments: bool):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.messageid: str = messageid
        self.includeattachments: bool = str(includeattachments)

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["messageId"] = self.messageid
        parameters["includeAttachments"] = self.includeattachments

        inputs["host"] = Outlook365GetEmailV2.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class Outlook365GetEmailsV3(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_office365",
        "connectionName": "shared_office365",
        "operationId": "GetEmailsV3"
    }

    def __init__(self, name: str, folderpath: str, fetchonlyunread: bool, includeattachments: bool, top: int, importance: str, fetchonlywithattachment: bool):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.folderpath: str = folderpath
        self.fetchonlyunread: bool = str(fetchonlyunread)
        self.includeattachments: bool = str(includeattachments)
        self.top: int = top
        self.importance: str = importance
        self.fetchonlywithattachment: bool = str(fetchonlywithattachment)

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["folderPath"] = self.folderpath
        parameters["fetchOnlyUnread"] = self.fetchonlyunread
        parameters["includeAttachments"] = self.includeattachments
        parameters["top"] = self.top
        parameters["importance"] = self.importance
        parameters["fetchOnlyWithAttachment"] = self.fetchonlywithattachment

        inputs["host"] = Outlook365GetEmailsV3.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class Outlook365MarkAsReadOrUnreadV3(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_office365",
        "connectionName": "shared_office365",
        "operationId": "MarkAsRead_V3"
    }

    def __init__(self, name: str, messageid: str):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.messageid: str = messageid

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["messageId"] = self.messageid

        inputs["host"] = Outlook365MarkAsReadOrUnreadV3.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class Outlook365MoveEmailV2(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_office365",
        "connectionName": "shared_office365",
        "operationId": "MoveV2"
    }

    def __init__(self, name: str, messageid: str, folderpath: str):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.messageid: str = messageid
        self.folderpath: str = folderpath

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["messageId"] = self.messageid
        parameters["folderPath"] = self.folderpath

        inputs["host"] = Outlook365MoveEmailV2.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class Outlook365ReplyToEmailV3(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_office365",
        "connectionName": "shared_office365",
        "operationId": "ReplyToV3"
    }

    def __init__(self, name: str, messageid: str, body: str):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.messageid: str = messageid
        self.body: str = body

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["messageId"] = self.messageid
        parameters["replyParameters/Body"] = self.body

        inputs["host"] = Outlook365ReplyToEmailV3.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class Outlook365SendEmailWithOptions(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_office365",
        "connectionName": "shared_office365",
        "operationId": "SendMailWithOptions"
    }

    def __init__(self, name: str, to: str, subject: str, options: str, importance: str, hidehtmlmessage: bool, showhtmlconfirmationdialog: bool, hidemicrosoftfooter: bool):
        super().__init__(name)
        self.type = "OpenApiConnectionWebhook"
        self.to: str = to
        self.subject: str = subject
        self.options: str = options
        self.importance: str = importance
        self.hidehtmlmessage: bool = str(hidehtmlmessage)
        self.showhtmlconfirmationdialog: bool = str(showhtmlconfirmationdialog)
        self.hidemicrosoftfooter: bool = str(hidemicrosoftfooter)

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["optionsEmailSubscription/Message/To"] = self.to
        parameters["optionsEmailSubscription/Message/Subject"] = self.subject
        parameters["optionsEmailSubscription/Message/Options"] = self.options
        parameters["optionsEmailSubscription/Message/Importance"] = self.importance
        parameters["optionsEmailSubscription/Message/HideHTMLMessage"] = self.hidehtmlmessage
        parameters["optionsEmailSubscription/Message/ShowHTMLConfirmationDialog"] = self.showhtmlconfirmationdialog
        parameters["optionsEmailSubscription/Message/HideMicrosoftFooter"] = self.hidemicrosoftfooter

        inputs["host"] = Outlook365SendEmailWithOptions.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d


class Outlook365SetUpAutomaticRepliesV2(BaseAction):
    connection_host = {
        "apiId": "/providers/Microsoft.PowerApps/apis/shared_office365",
        "connectionName": "shared_office365",
        "operationId": "SetAutomaticRepliesSetting_V2"
    }

    def __init__(self, name: str, status: str, externalaudience: str):
        super().__init__(name)
        self.type = "OpenApiConnection"
        self.status: str = status
        self.externalaudience: str = externalaudience

    def export(self) -> Dict:
        inputs = {}
        parameters = {}

        parameters["body/automaticRepliesSetting/status"] = self.status
        parameters["body/automaticRepliesSetting/externalAudience"] = self.externalaudience

        inputs["host"] = Outlook365SetUpAutomaticRepliesV2.connection_host
        inputs["parameters"] = parameters

        d = {}
        d["metadata"] = self.metadata
        d["type"] = self.type
        d["runAfter"] = self.runafter
        d["inputs"] = inputs

        return d

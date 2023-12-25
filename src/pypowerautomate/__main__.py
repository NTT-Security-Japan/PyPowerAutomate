import argparse

from pypowerautomate.package import Package
from pypowerautomate.flow import Flow
from pypowerautomate.triggers import ManualTrigger
from pypowerautomate.actions import ListUserEnvironmentsAction, ListConnectionsAction

DUMMY_FLOWMANAGEMENT_ID = "shared-flowmanagemen-12345678-90ab-cdef-1234-567890abcdef"

def main():
    """
    The main function that generates a test flow for the Microsoft Power Automate CLI.

    The flow consists of two actions:
    1. ListUserEnvironmentsAction: Retrieves the list of user environments.
    2. ListConnectionsAction: Retrieves the list of connections.

    The flow is triggered by a manual trigger (a button).

    The function also handles command-line arguments:
    - `--name` (or `-n`): The name of the flow, defaults to "GetUserEnvironmentsFlow".
    - `--flowmanagement_id` (or `-f`): The connection ID for the Power Automate Management connector. If not provided, a dummy ID is used.

    The generated flow is exported as a ZIP file.
    """
    parser = argparse.ArgumentParser(
        prog="python -m pac2", description="PyPowerAutomate CLI (only for test)")

    parser.add_argument("-n", "--name", type=str, default="GetUserEnvironmentsFlow", help="Flow name.")
    parser.add_argument("-f", "--flowmanagement_id", type=str, help="Connection ID for PowerAutomate Managemet Connector")

    args = parser.parse_args()

    if not args.flowmanagement_id:
        print("[+] Generete test flow with dummy flowmanagement ID.")
        args.flowmanagement_id = DUMMY_FLOWMANAGEMENT_ID
    else:
        print(f"[+] Generete test flow with flowmanagement ID: {args.flowmanagement_id}")

    # Generate following test flow
    #         +-------+
    #         | Start |
    #         +---+---+
    #             |
    #      +------+---------+
    #      |                |
    # +----v--------+  +----v-----------+
    # | ListUserEnv |  | ListConnection |
    # +-------------+  +----------------+

    # init the flow
    flow = Flow()

    flow.set_trigger(ManualTrigger("Button"))

    flow.add_top_action(ListUserEnvironmentsAction("ListUserEnvironments"))
    flow.add_top_action(ListConnectionsAction("ListConnectionsAction"))

    package = Package("TestFlow", flow)
    package.set_flow_management_connector(args.flowmanagement_id)
    package.export_zipfile()


if __name__ == "__main__":
    main()

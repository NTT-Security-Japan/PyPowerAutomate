# PyPowerAutomate

*PyPowerAutomate is not affiliated with Microsoft Corporation.*

## Overview

PyPowerAutomate is a Python package designed for creating, managing, and deploying Microsoft Power Automate Flows programmatically. This library provides a simple and efficient way to define Power Automate Flows in JSON format directly from Python code. Whether you're an automation expert, a developer looking to integrate Power Automate into your Python projects, or an enthusiast exploring the realms of workflow automation, Power Automate Library is your go-to tool.

## Features

- **Flow Creation**: Easily define and create Power Automate flows in JSON format.
- **Package Creation**: Easily create a legacy package that could import to Power Automate Platform
- **Customization**: Tailor your flows with dynamic parameters and custom logic.
- **Compatibility**: Seamless integration with existing Power Automate infrastructure.

## Installation

To install PyPowerAutomate, run the following command in your terminal:

```bash
pip install PyPowerAutomate
```

## Quick Start

Here's a simple example to get you started:

```python
from pypowerautomate.flow import Flow
from pypowerautomate.triggers import ManualTrigger
from pypowerautomate.actions import InitVariableAction,IncrementVariableAction,VariableTypes
from pypowerautomate.package import Package

flow = Flow()

flow.set_trigger(ManualTrigger("Button"))

flow.add_top_action(InitVariableAction("action1","a",VariableTypes.integer,1))
flow.append_action(IncrementVariableAction("action2","a",2))

package = Package("incremental_test",flow)
package.export_zipfile()
```

This example creates manual trigger and 2 actions. Then export the flow as legacy package(zip file).
You can import the flow by uploading `incremental_test.zip` to Power Automate. 

## Supported Triggers

- Manual Trigger
- Schedule Trigger

## Supported Build-in Actions

- Variable
- Conditionals
- Loops
- Data Operations
- Time
- HTTP (requires Premium subscription)

## Supported Connectors

Currently, PyPowerAutomate supports following connectors.

- [Power Automate Management](https://powerautomate.microsoft.com/en-us/connectors/details/shared_flowmanagement/power-automate-management/)
- [Approvals](https://powerautomate.microsoft.com/en-us/connectors/details/shared_approvals/approvals/)
- [Office 365 Outlook](https://powerautomate.microsoft.com/en-us/connectors/details/shared_office365/office-365-outlook/)
- [SharePoint](https://powerautomate.microsoft.com/en-us/connectors/details/shared_sharepointonline/sharepoint/)
- [Dropbox](https://powerautomate.microsoft.com/en-us/connectors/details/shared_dropbox/dropbox/)
- [Teams](https://powerautomate.microsoft.com/en-us/connectors/details/shared_teams/microsoft-teams/)

## Documentation

[Documentation of PyPowerAutomate](https://ntt-security-japan.github.io/PyPowerAutomate/)

## Contributing

Thank you for considering contributing to this project! We welcome all contributions, from minor fixes to major features. To ensure effective and smooth collaboration, please follow these guidelines:

### Contributing Code

1. Check and Open Issues: Before contributing, please check if there are existing issues on GitHub related to your problem or suggestion. If not, open a new one and share the details.

2. Pull Requests: If you want to make changes, first fork the repository, create a branch for your topic, and then submit a pull request. In your pull request, clearly explain what changes you made and why.

3. Code Review: The project maintainers will review your pull request. If there are any comments, please respond to them actively.

### Code of Conduct

We aim to provide all contributors and maintainers with a safe and positive experience. Therefore, we ask you to follow this code of conduct, which is based on the Contributor Covenant:

- Respect Each Other: Treat everyone working on the project respectfully, regardless of background.

- Promote Inclusively: Actively promote inclusively and welcome diverse perspectives.

- Maintain a Harassment-Free Environment: Avoid any behavior seen as harassment and maintain a harassment-free environment.

## License

PyPowerAutomate is licensed under the BSD-3-clause license. See [LICENSE](https://github.com/NTT-Security-Japan/PyPowerAutomate/LICENSE) for more details.

---

Happy Automating! 🚀

---


---
layout: "cdktf"
page_title: "CLI Configuration"
sidebar_current: "cdktf"
description: "Install and configure the CDKTF Command Line Interface."
---

# CLI Configuration

-> **Note:** CDK for Terraform is currently in [beta](/docs/cdktf/index.html#project-maturity-and-production-readiness).

The CDK for Terraform (CDKTF) CLI allows you to initialize a new CDKTF project, adjust project settings, synthesize your infrastructure into Terraform configuration files, deploy your CDKTF application, and more. You can also use some Terraform CLI commands like `terraform apply` and `terraform destroy` directly, but we recommend using the available [`cdktf cli` commands](/docs/cdktf/cli-reference/commands.html) where possible.

## Install

```bash
$ npm install -g cdktf-cli
```

## Use

```bash
$ cdktf --help
```

Help output:

```
Commands:
  cdktf convert [OPTIONS]          Converts a single file of HCL configuration to Terraform CDK. Takes the file to be converted on stdin.
  cdktf deploy [stack] [OPTIONS]   Deploy the given stack                                                                                                                                                   [aliases: apply]
  cdktf destroy [stack] [OPTIONS]  Destroy the given stack
  cdktf diff [stack] [OPTIONS]     Perform a diff (terraform plan) for the given stack                                                                                                                       [aliases: plan]
  cdktf get [OPTIONS]              Generate CDK Constructs for Terraform providers and modules.
  cdktf init [OPTIONS]             Create a new cdktf project from a template.
  cdktf list [OPTIONS]             List stacks in app.
  cdktf login                      Retrieves an API token to connect to Terraform Cloud.
  cdktf synth [stack] [OPTIONS]    Synthesizes Terraform code for the given app in a directory.                                                                                                        [aliases: synthesize]
  cdktf completion                 generate completion script

Options:
  --version                   Show version number                                                                                                                                                                  [boolean]
  --disable-logging           Dont write log files. Supported using the env CDKTF_DISABLE_LOGGING.                                                                                                 [boolean] [default: true]
  --disable-plugin-cache-env  Dont set TF_PLUGIN_CACHE_DIR automatically. This is useful when the plugin cache is configured differently. Supported using the env CDKTF_DISABLE_PLUGIN_CACHE_ENV. [boolean] [default: false]
  --log-level                 Which log level should be written. Only supported via setting the env CDKTF_LOG_LEVEL                                                                                                 [string]
  -h, --help                  Show help                                                                                                                                                                            [boolean]

Options can be specified via environment variables with the "CDKTF_" prefix (e.g. "CDKTF_OUTPUT")
```

### CI Environment

If you are running the CLI in an automated environment, you can force the dynamic CLI output rendering to be static by setting the `CI` environment variable to `true`.

## Configuration File

You can configure the behavior of the Terraform CDK CLI by modifying the `cdktf.json` file in your project root directory. Refer to the [cdktf.json documentation](/docs/cdktf/create-and-deploy/configuration-file.html) for more detail on how you can supply custom configuration settings for your application.

## Telemetry

The CDKTF CLI ([cdktf-cli](https://github.com/hashicorp/terraform-cdk/tree/main/packages/cdktf-cli) interacts with a HashiCorp service called [Checkpoint](https://checkpoint.hashicorp.com)
to report project metrics such as cdktf version, project language, provider name, platform name, and other details that help guide the project maintainers with feature and roadmap decisions. The [code that interacts with Checkpoint](https://github.com/hashicorp/terraform-cdk/tree/main/packages/cdktf-cli/lib/checkpoint.ts) is part of the CDK for Terraform CLI.

The use of Checkpoint is completely optional. Refer to the [telemetry documentation](/docs/cdktf/telemetry.html) for more information about Checkpoint and you can disable it if desired.
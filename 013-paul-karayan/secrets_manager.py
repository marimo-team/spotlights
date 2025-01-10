# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
# ]
# ///

import marimo

__generated_with = "0.10.10"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
        ## AWS Secrets Manager Utils

        Wow - we can write a secret to multiple envs! But that's not really the point. 

        This example shows that  with Marimo that you can quickly have:
        ```
        - a CLI 
        - a GUI "micro app"
        - a notebook
        ```

        with little change to the base code.
        """
    )
    return


@app.cell
def _():
    import subprocess
    import marimo as mo

    def bash(command):
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    return bash, mo, subprocess


@app.cell
def _(profiles):
    def generate_aws_secrets_commands(secret_name, secret_string):
        environments = ['dev', 'stage', 'prod']

        region = 'us-west-2'


        output = ["Now youre good:\n\n"]
        print(str(output))
        for env in environments:
            profile = profiles[env]
            aws_command = (f"""aws secretsmanager create-secret --region {region} --name '/{secret_name}' --secret-string '{secret_string}'"""
            )
            print(aws_command)
            output.append(aws_command+"\n")

        return output
    return (generate_aws_secrets_commands,)


@app.cell
def _(mo):
    # create the gui
    form = (
            mo.md('''
            **GUI**

            {secret_name}
            {secret_string}
        ''')
        .batch(
            secret_name=mo.ui.text(label="Secret Name - \n", placeholder="/NAME"),
            secret_string=mo.ui.text(label="Secret (actual string)"),
        )
        .form()
    )
    return (form,)


@app.cell
def _(form, mo):
    mo.vstack([form, mo.md(f"Has value: {form.value}")])
    return


@app.cell
def _(form, generate_aws_secrets_commands, mo):
    if mo.cli_args():
        output = ""
        generate_aws_secrets_commands(
            mo.cli_args().get("secret_name"), mo.cli_args().get("secret_string")
        )

    elif form.value:
        form_value = form.value
        output = generate_aws_secrets_commands(
            form_value.get("secret_name"), form_value.get("secret_string")
        )

    else:
        output = ""

    output
    return form_value, output


@app.cell
def _(mo, output):
    mo.md("\n".join(output))
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()

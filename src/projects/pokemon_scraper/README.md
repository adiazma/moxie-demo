# CBRE Scraper

To get the latest driver use the next link:

```
https://developer.microsoft.com/es-es/microsoft-edge/tools/webdriver/?form=MA13LH#downloads
```

In addition, to activate the .venv, use the next command:

```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Execution

The Rubi integration has the following settings within the `--function` field.

- `run_calendar`: Updates the calendar based on the information present in `config.json`, and first cleans the entire calendar with the default ON and OFF date. The following example updates the off and on values ​​of the calendar for Monday and Tuesday respectively, through the command `--project=cbre_scraper --function=run_calendar` the value of the `principal` machine.

```
{
    "point_ref": "produccion",
    "update_days": [
        {
            "status": "on",
            "ventilador": null,
            "setpoint": null,
            "week_day": "6",
            "hour": "6:30"
        },
        {
            "status": "off",
            "ventilador": null,
            "setpoint": null,
            "week_day": "6",
            "hour": "20:00"
        }
    ]
}
```

- `run_machine`: Executes an action within the machine based on the information present in `config.json`. In the following example, uta 1 and 2 are turned on respectively.

```
{
    "status": "on", 
    "machines": [
        "Vestibulo 1"
    ]
}
```
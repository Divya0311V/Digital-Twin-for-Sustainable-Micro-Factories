import pathway as pw

class MachineSchema(pw.Schema):
    timestamp: str
    machine: str
    temperature: float
    vibration: float
    power: float
    load: float
    carbon: float

table = pw.io.csv.read(
    "factory_data.csv",
    schema=MachineSchema,
    mode="streaming",
)

windowed = table.windowby(
    table.machine,
    pw.temporal.tumbling(duration=10)
).reduce(
    avg_power=pw.reducers.avg(table.power),
    total_carbon=pw.reducers.sum(table.carbon),
    avg_load=pw.reducers.avg(table.load),
    max_temp=pw.reducers.max(table.temperature),
    max_vibration=pw.reducers.max(table.vibration),
)

result = windowed.select(
    windowed.machine,
    windowed.avg_power,
    windowed.total_carbon,
    efficiency=windowed.avg_load / windowed.avg_power,
    sustainability_score=100 - (windowed.avg_power * 5),
    alert=pw.if_else(
        windowed.avg_power > 7,
        "⚠ Power Spike",
        pw.if_else(
            windowed.max_vibration > 0.8,
            "⚠ High Vibration",
            pw.if_else(
                windowed.max_temp > 85,
                "⚠ Overheating",
                "Normal"
            )
        )
    ),
    suggestion=pw.if_else(
        windowed.avg_power > 7,
        "Reduce load by 15%",
        pw.if_else(
            windowed.max_vibration > 0.8,
            "Schedule maintenance check",
            pw.if_else(
                windowed.max_temp > 85,
                "Activate cooling system",
                "Operating Normally"
            )
        )
    )
)

pw.io.stdout.write(result)

pw.run()

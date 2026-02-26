import pathway as pw

class FactorySchema(pw.Schema):
    machine_id: str
    energy_usage: int
    temperature: int
    carbon_emission: int
    production_load: int

data = pw.io.csv.read(
    "factory_stream.csv",
    schema=FactorySchema,
    mode="streaming",
)

energy_stats = data.groupby(data.machine_id).reduce(
    avg_energy=pw.reducers.avg(data.energy_usage),
    max_temp=pw.reducers.max(data.temperature),
    avg_load=pw.reducers.avg(data.production_load),
)

alerts = data.select(
    machine_id=data.machine_id,
    energy_usage=data.energy_usage,
    temperature=data.temperature,
    carbon_emission=data.carbon_emission,
    production_load=data.production_load,
    alert_type=pw.if_else(
        data.temperature > 90,
        "CRITICAL TEMP",
        pw.if_else(
            data.energy_usage > 150,
            "HIGH ENERGY",
            pw.if_else(
                data.production_load > 95,
                "OVERLOAD",
                "NORMAL"
            )
        )
    )
)

alerts = alerts.filter(pw.this.alert_type != "NORMAL")

sustainability = data.select(
    machine_id=data.machine_id,
    sustainability_score=100 - (
        (data.energy_usage / 200) * 30 +
        (data.carbon_emission / 100) * 70
    )
)

pw.io.csv.write(alerts, "live_alerts.csv")
pw.io.csv.write(sustainability, "live_sustainability.csv")
pw.io.csv.write(energy_stats, "live_energy_stats.csv")

pw.run()

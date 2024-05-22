import sys
from pathlib import Path

# Add parent path to Python path to be able to import modules
current_dir = Path(__file__).parent.absolute()
app_dir = current_dir.parent.parent
sys.path.insert(0, str(app_dir))

from app import create_app
from utils.logger import logger
import psutil

from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import ConsoleMetricExporter, PeriodicExportingMetricReader
from opentelemetry.sdk.metrics._internal.instrument import CallbackOptions, Measurement

metric_reader = PeriodicExportingMetricReader(ConsoleMetricExporter())
provider = MeterProvider(metric_readers=[metric_reader])

metrics.set_meter_provider(provider)
meter = metrics.get_meter(__name__)


def cpu_usage_callback(options: CallbackOptions):
    return [Measurement(psutil.cpu_percent(), {"state": "cpu_usage"})]


def memory_usage_callback(options: CallbackOptions):
    return [Measurement(psutil.virtual_memory().percent, {"state": "memory_usage"})]


meter.create_observable_gauge(
    name="cpu_usage",
    description="CPU Usage",
    unit="percent",
    callbacks=[cpu_usage_callback]
)

meter.create_observable_gauge(
    name="memory_usage",
    description="Memory Usage",
    unit="percent",
    callbacks=[memory_usage_callback]
)

logs = logger.get_module_logger("ORCHESTRATOR")
logs.info("Orchestrator started")
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')

import logging
from pathlib import Path

def get_logger(name: str = "student_app") -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        logger.addHandler(console)
        log_dir = Path("logs")
        try:
            log_dir.mkdir(exist_ok=True)
            file_handler = logging.FileHandler(log_dir / "student_app.log", encoding="utf-8")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        except OSError:
            logger.warning("Could not create file log; continuing with console logging.")
    return logger

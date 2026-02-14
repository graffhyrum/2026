"""
Generate the conference schedule markdown from YAML data.

This module provides an MkDocs hook that automatically generates
docs/schedule/index.md from data/schedule.yaml during the build process.
"""

import yaml
from pathlib import Path


def format_title_with_link(title: str, link: str | None, speaker: str | None) -> str:
    """Format a schedule item title with optional link and speaker."""
    if link:
        formatted_title = f"[{title}]({link})"
        if speaker:
            formatted_title += f"<br/>{speaker}"
        return formatted_title
    elif speaker:
        return f"{title}<br/>{speaker}"
    else:
        return title


def format_time(time_str: str) -> str:
    """Format time string to use non-breaking spaces."""
    return time_str.replace(" AM", "&nbsp;AM").replace(" PM", "&nbsp;PM")


def generate_friday_table(items: list[dict]) -> str:
    """Generate the Friday tutorial table."""
    lines = []
    lines.append("| Time              |                                     Tutorial                                      |  Instructor  |")
    lines.append("| :---------------- | :-------------------------------------------------------------------------------: | :----------: |")
    
    for item in items:
        time = item["time"]
        title = item["title"]
        link = item.get("link")
        speaker = item.get("speaker") or ""
        
        if link:
            formatted_title = f"[{title}]({link})"
        else:
            formatted_title = title
        
        lines.append(f"| {time} | {formatted_title} | {speaker} |")
    
    return "\n".join(lines)


def generate_weekend_table(items: list[dict], day_name: str) -> str:
    """Generate the Saturday or Sunday table."""
    lines = []
    lines.append(f"| Time {{: ^ .table }} | {day_name} |")
    lines.append("| :----------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |")
    
    for item in items:
        time = format_time(item["time"])
        title = item["title"]
        link = item.get("link")
        speaker = item.get("speaker")
        
        formatted_title = format_title_with_link(title, link, speaker)
        lines.append(f"| {time} | {formatted_title} |")
    
    return "\n".join(lines)


def generate_schedule():
    """Generate the schedule markdown file from YAML data."""
    # Read the YAML data
    yaml_path = Path("data/schedule.yaml")
    with open(yaml_path, "r") as f:
        data = yaml.safe_load(f)
    
    # Generate the markdown content
    content = """---
Title: Full Schedule
description: A full schedule grid for the event
---

# Schedule

## Friday

"""
    
    # Add Friday table
    content += generate_friday_table(data["friday"])
    content += "\n\n"
    
    # Add Saturday table
    content += "## Saturday\n\n"
    content += generate_weekend_table(data["saturday"], "Saturday")
    content += "\n\n"
    
    # Add Sunday table
    content += "## Sunday\n\n"
    content += generate_weekend_table(data["sunday"], "Sunday")
    content += "\n"
    
    # Write the generated content
    output_path = Path("docs/schedule/index.md")
    with open(output_path, "w") as f:
        f.write(content)
    
    print(f"✓ Generated {output_path}")
    print(f"✓ Schedule contains {len(data['friday'])} Friday items, "
          f"{len(data['saturday'])} Saturday items, and {len(data['sunday'])} Sunday items")


def on_pre_build(config):
    """MkDocs hook: Generate schedule before building the site."""
    generate_schedule()

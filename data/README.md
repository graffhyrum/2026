# Schedule Data Management

## Overview

The PyTexas 2026 conference schedule is managed using a **data-driven approach** to make updates easier and reduce the pain of editing complex markdown tables.

## How It Works

- **`schedule.yaml`** - The source of truth for all schedule data (this directory)
- **`hooks/schedule.py`** - MkDocs hook that auto-generates the schedule during build
- **`docs/schedule/index.md`** - The generated schedule page (DO NOT EDIT DIRECTLY)

### Workflow

1. **Edit the schedule**: Modify `schedule.yaml` with your changes
2. **Build/serve the site**: Run `just serve` or `just build`
3. **Schedule auto-regenerates**: The MkDocs `on_pre_build` hook generates the markdown automatically

## Editing the Schedule

### Adding a Talk

```yaml
saturday:
  - time: "10:20 AM"
    title: "Your Talk Title"
    link: "talks.md#your-talk-anchor"
    speaker: "Speaker Name"
```

### Adding a Break or Event

```yaml
saturday:
  - time: "10:05 AM"
    title: "15 Minute Break"
    speaker: null
```

### Moving Time Slots

Simply change the time in the YAML - no need to reformat tables!

```yaml
# Before
  - time: "10:20 AM"
    title: "Some Talk"
    
# After  
  - time: "10:30 AM"
    title: "Some Talk"
```

### Reordering Sessions

Just move the YAML blocks around in the desired order.

## Benefits

✅ **Easy to edit** - Change times without reformatting tables  
✅ **Less error-prone** - YAML structure prevents markdown table formatting issues  
✅ **Version control friendly** - Cleaner diffs showing actual changes  
✅ **Consistent formatting** - Generator ensures uniform output  
✅ **Automatic regeneration** - No manual script running needed

## Tips

- Keep the YAML file well-organized with consistent spacing
- Use `null` for speaker field when there's no speaker (breaks, lunch, etc.)
- The `link` field is optional - omit it for items without talk pages
- Time formats should be consistent within each day
- Schedule constraints and notes are documented in comments at the top of `schedule.yaml`

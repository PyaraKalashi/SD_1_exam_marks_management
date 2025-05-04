# University Grading Calculator - README  

## Overview  
This Python-based application predicts student progression outcomes (Progress, Trailer, Retriever, Exclude) based on credit inputs. It features robust validation, multiple operation modes, and visual data representation.

## Key Features
- **Dual Operation Modes**:
  - Student Mode: Single outcome prediction
  - Staff Mode: Batch processing with visualization
- **Comprehensive Validation**:
  - Integer and range checking (0-120 credits)
  - Total credit verification (must sum to 120)
- **Data Visualization**:
  - Color-coded histogram showing outcome distribution
  - Automatic scaling for any number of results
- **Data Persistence**:
  - In-memory storage (lists)
  - File output (records.txt)

## Technical Specifications
- **Core Logic**: 28 progression rules condensed to 4 efficient categories
- **Visualization**: Built with graphics.py library
- **Error Handling**: Custom messages for all invalid cases
- **Data Structures**: Nested lists for input storage

## Usage Examples
### Sample Output
```
Progress - 120, 0, 0
Progress (module trailer) - 100, 20, 0
Module retriever - 80, 40, 0
Exclude - 40, 0, 80
```

### Histogram Features
- Bars represent outcome counts
- Color differentiation for quick analysis
- Total outcomes displayed

## Getting Started
1. Ensure Python 3.x and graphics.py are installed
2. Run either:
   - `python w2052776_part1.py` (basic version)
   - `python w2052776_part2_part3.py` (extended version)
3. Follow on-screen prompts

## Development Notes
- **Modular Design**: Separated validation, logic, and UI components
- **Extensible**: Easy to add new features like database integration
- **Commented Code**: Over 30 explanatory comments in main files

## Academic Context
Developed for University of Westminster's Software Development I course (4COSC006C.1) demonstrating:
- Algorithm design
- Data processing
- User interface principles
- Documentation standards

## License
MIT License - See LICENSE file for details

---



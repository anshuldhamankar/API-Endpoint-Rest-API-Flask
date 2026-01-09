# Wimbledon Finals API

A simple Flask REST API for practicing API endpoints. Returns Wimbledon tennis finals data by year.

## Setup

```bash
pip install -r requirements.txt
python run.py
```

## Endpoints

### GET /
Welcome message with usage instructions.

### GET /wimbledon?year=YYYY
Returns Wimbledon finals data for the specified year.

**Parameters:**
- `year` (required): Year as a 4-digit number

**Example:**
```bash
curl "http://localhost:5000/wimbledon?year=2023"
```

**Response:**
```json
{
  "year": 2023,
  "champion": "Novak Djokovic",
  "runner_up": "Carlos Alcaraz",
  "score": "1-6, 7-6, 6-1, 3-6, 6-4",
  "sets": 5,
  "tiebreak": true
}
```

## Error Responses
- `400`: Missing or invalid year parameter
- `404`: No data found for the specified year
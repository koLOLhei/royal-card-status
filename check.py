"""Public endpoints only. Never reads application/customer data or credentials."""
import json
import time
import urllib.request

checks = [
    ('API', 'https://royal-card-api.soara-mu.jp/api/health'),
    ('Website', 'https://royal-card.soara-mu.jp/'),
]
failures = []
for name, url in checks:
    for attempt in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'RoyalCard-AvailabilityCheck/1.0'})
            with urllib.request.urlopen(req, timeout=15) as response:
                body = response.read(2_000_000)
                assert response.status == 200
            if name == 'API':
                data = json.loads(body)
                assert data.get('ok') is True and data.get('mode') == 'app_store'
            else:
                assert any(title in body.decode('utf-8') for title in ('The Royal Card', 'THE ROYAL CARD', 'ザロイヤルカード'))
            print(name + ': OK')
            break
        except Exception as error:
            if attempt == 2:
                failures.append(name + ': ' + type(error).__name__)
            else:
                time.sleep(10)
if failures:
    raise SystemExit('\n'.join(failures))

# 1. Check if artist key exists in festival_schedule using O(1) hash lookup
# 2. If found, return the associated value
# 3. Otherwise, return {'message': 'Artist not found'}
# 
# Time: O(1)
# Space: O(1)
    
def prob02(artist: str, festival_schedule: dict[str, dict[str, str]]) -> dict[str, str]:
    if artist in festival_schedule:
        return festival_schedule[artist]
    else:
        return { 'message': 'Artist not found' }

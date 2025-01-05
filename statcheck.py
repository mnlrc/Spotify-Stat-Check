import json
import time


def readSpotifyStats(stats):
    with open("Streaming_History_Audio_2024-2025_9.json", "r") as f:
        data = json.load(f)

        for dictVals in data:
            artist_name = dictVals.get("master_metadata_album_artist_name", "Unknown Artist")
            track_name = dictVals.get("master_metadata_track_name", "Unknown Track")

            # Adding new artist
            if artist_name not in stats:
                stats[artist_name] = {}

            # Adding song or incrementing
            if track_name not in stats[artist_name]:
                stats[artist_name][track_name] = 1
            else:
                stats[artist_name][track_name] += 1



def main():
    stats = {}
    readSpotifyStats(stats)

    for artist, songs in stats.items():
        print(f"Artist: {artist}")
        for song, count in songs.items():
            print(f"  Song: {song}, {count}x")
        print()


if __name__ == "__main__":
    main()

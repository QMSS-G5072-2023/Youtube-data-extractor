import sys
sys.path.append("/Users/mcbookpro/youtube_data_extractor")

import pytest
from youtube_data_extractor.youtube_data_extractor import extract_translatable_languages_and_count
from youtube_data_extractor.youtube_data_extractor import extract_extract_quality_and_audio
from youtube_data_extractor.youtube_data_extractor import extract_links

import pandas as pd

def test_extract_translatable_languages_and_count():
    # Create a mock DataFrame
    data = {'caption': [{'captionTracks': [{'name': 'English', 'isTranslatable': True},
                                          {'name': 'Spanish', 'isTranslatable': False}]}]}
    df = pd.DataFrame(data)

    # Call the function
    languages, count = extract_translatable_languages_and_count(df)

    # Assertions
    assert 'English' in languages
    assert count == 1

    
    
def test_extract_quality_and_audio():
    # Mock data
    data = {'formats': [{'qualityLabel': '720p', 'audioQuality': 'medium'},
                        {'qualityLabel': '1080p', 'audioQuality': 'high'}]}
    df = pd.DataFrame(data)

    # Call the function
    quality_audio = extract_quality_and_audio(df)

    # Assertions
    assert ('720p', 'medium') in quality_audio
    assert ('1080p', 'high') in quality_audio

    
def test_extract_links():
    # Mock data
    data = {'description': ['Check out this link: https://example.com',
                            'Visit our website at https://site.com']}
    df = pd.DataFrame(data)

    # Call the function
    links = extract_links(df)

    # Assertions
    assert 'https://example.com' in links
    assert 'https://site.com' in links

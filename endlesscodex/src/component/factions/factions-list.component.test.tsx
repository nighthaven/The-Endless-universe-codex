import { render, screen, waitFor } from '@testing-library/react';
import axios from 'axios';
import configureStore from 'redux-mock-store';
import { Provider } from 'react-redux';
import FactionListComponent from './factions-list.component';

const mockStore = configureStore();
const store = mockStore({
  background: {},
  item: {},
});

jest.mock('axios');
const mockedAxios = axios as jest.Mocked<typeof axios>;

test('faction-list component renders factions', async () => {
  const mockFactions = [
    {
      id: 1,
      faction: { name: 'Faction 1' },
      media: { name: 'Media 1' },
      description: 'Description for Faction 1',
      image_url: 'image1.jpg',
      government: 'Government 1',
      ideology: 'Ideology 1',
      home_planet: 'Planet 1',
      affinity: ['Affinity 1'],
      populations: ['Population 1'],
      traits: ['Trait 1'],
      starting_technology: ['Technology 1'],
      units: ['Unit 1'],
      heroes: ['Hero 1'],
      major: true,
    },
  ];

  mockedAxios.get.mockResolvedValueOnce({ data: mockFactions });

  render(
    <Provider store={store}>
      <FactionListComponent />
    </Provider>
  );

  await waitFor(() => {
    const factionListElement = screen.getByTestId('faction');
    expect(factionListElement).toBeInTheDocument();
  });

  expect(screen.getByText('Faction 1')).toBeInTheDocument();
});

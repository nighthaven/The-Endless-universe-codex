import { render, screen } from '@testing-library/react';
import configureStore from 'redux-mock-store';
import { Provider, useDispatch } from 'react-redux';
import { MemoryRouter } from 'react-router-dom';
import WondersPage from './wonders-page.component';
import Mock = jest.Mock;

jest.mock('react-redux', () => ({
  ...jest.requireActual('react-redux'),
  useDispatch: jest.fn(),
}));

const mockStore = configureStore();
const store = mockStore({
  background: { fireflies: [] },
  item: {},
  wonders: {
    wonders: [
      {
        id: 1,
        name: 'wonder',
        description: 'wonder description',
        image: 'wonderImage1.png',
      },
    ],
  },
});

test('wonders page component', () => {
  const mockDispatch = jest.fn();
  (useDispatch as unknown as Mock).mockReturnValue(mockDispatch);
  render(
    <Provider store={store}>
      <MemoryRouter>
        <WondersPage />
      </MemoryRouter>
    </Provider>
  );

  const wonderPageElement = screen.getByTestId('wonder-content');
  expect(wonderPageElement).toBeInTheDocument();
});

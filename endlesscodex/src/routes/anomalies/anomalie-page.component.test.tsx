import { render, screen } from '@testing-library/react';
import configureStore from 'redux-mock-store';
import { Provider, useDispatch } from 'react-redux';
import { MemoryRouter } from 'react-router-dom';
import AnomaliesPage from './anomalies-page.component';
import Mock = jest.Mock;

jest.mock('react-redux', () => ({
  ...jest.requireActual('react-redux'),
  useDispatch: jest.fn(),
}));

const mockStore = configureStore();
const store = mockStore({
  background: { fireflies: [] },
  item: {},
  anomalies: {
    anomalies: [
      {
        id: 1,
        name: 'anomaly',
        description: 'anomaly description',
        image: 'anomalyImage1.png',
      },
    ],
  },
});

test('anomalies page component', () => {
  const mockDispatch = jest.fn();
  (useDispatch as unknown as Mock).mockReturnValue(mockDispatch);
  render(
    <Provider store={store}>
      <MemoryRouter>
        <AnomaliesPage />
      </MemoryRouter>
    </Provider>
  );

  const anomaliePageElement = screen.getByTestId('anomalie-content');
  expect(anomaliePageElement).toBeInTheDocument();
});

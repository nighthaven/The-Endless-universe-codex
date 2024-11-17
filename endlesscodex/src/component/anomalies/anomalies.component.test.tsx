import { render, screen } from '@testing-library/react';
import configureStore from 'redux-mock-store';
import { Provider, useDispatch } from 'react-redux';
import AnomaliesComponent from './anomalies.component';
import Mock = jest.Mock;

jest.mock('react-redux', () => ({
  // mock react redux en faisant un faux redux
  ...jest.requireActual('react-redux'), // met vrai react redux
  useDispatch: jest.fn(), // SAUF remplace useDispatch obligatoire en fonctionnel
}));

const mockStore = configureStore();
const store = mockStore({
  background: {},
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

test('anomalies component render', () => {
  const mockDispatch = jest.fn();
  (useDispatch as unknown as Mock).mockReturnValue(mockDispatch); // j'utilise useDispatch qui est mocké, react cherche le vrai dispatch donc unknown pour dire qu'on ne connait pas le type puis on force le type mock

  render(
    <Provider store={store}>
      <AnomaliesComponent />
    </Provider>
  );
  const anomalieElements = screen.getAllByTestId('anomalie-name');
  expect(anomalieElements.length).toEqual(1);
});

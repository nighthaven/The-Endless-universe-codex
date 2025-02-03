import { render, screen } from '@testing-library/react';
import configureStore from 'redux-mock-store';
import { Provider, useDispatch } from 'react-redux';
import WondersComponent from './wonders.component';
import Mock = jest.Mock;

jest.mock('react-redux', () => ({
  ...jest.requireActual('react-redux'),
  useDispatch: jest.fn(),
}));

const mockStore = configureStore();
const store = mockStore({
  background: {},
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

test('wonder component render', () => {
  const mockDispatch = jest.fn();
  (useDispatch as unknown as Mock).mockReturnValue(mockDispatch);

  render(
    <Provider store={store}>
      <WondersComponent />
    </Provider>
  );
  const wonderElements = screen.getAllByTestId('wonder-name');
  expect(wonderElements.length).toEqual(1);
});

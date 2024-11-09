import { render, screen } from '@testing-library/react';
import configureStore from 'redux-mock-store';
import { Provider } from 'react-redux';
import { MemoryRouter } from 'react-router-dom';
import AboutComponent from './about-page.component';

const mockStore = configureStore();
const store = mockStore({
  background: { fireflies: [] },
  item: {},
});

test('About page component', () => {
  render(
    <Provider store={store}>
      <MemoryRouter>
        <AboutComponent />
      </MemoryRouter>
    </Provider>
  );
  const aboutElement = screen.getByTestId('about-content');
  expect(aboutElement).toBeInTheDocument();
});

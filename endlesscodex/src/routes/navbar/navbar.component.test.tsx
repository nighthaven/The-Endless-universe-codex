import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import NavbarComponent from './navbar.component';

test('renders correctly', () => {
  render(
    <MemoryRouter>
      <NavbarComponent />
    </MemoryRouter>
  );
  const navigationElement = screen.getByTestId('navbar');
  expect(navigationElement).toBeInTheDocument();
});

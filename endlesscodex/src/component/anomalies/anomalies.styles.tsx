import styled from 'styled-components';

export const ImageContainerAnomaly = styled.div`
  width: 100%;
  max-width: 20%;
  height: 150px;
  flex: 1 1 auto;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 1px solid black;
  margin: 0 20px 15px;
  overflow: hidden;
`;

export const ImageBackground = styled.div<{ imageUrl: string }>`
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  background-image: ${({ imageUrl }) => `url(${imageUrl})`};
`;

export const InfoContainer = styled.div`
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 90%;
  position: relative;
  border-radius: 0.5rem;
  overflow: hidden;
  padding: 1.5rem;
  background-color: rgba(0, 0, 0, 0.2);
  border: 1px solid rgba(253, 100, 0, 0.5);
  backdrop-filter: blur(6px);
  box-shadow: inset 0 4px 6px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease;
  margin: 20px auto;

  h2 {
    color: #fd6400;
    min-width: 15%;
    margin-right: 20px;
  }

  p {
    color: #ffffff;
    font-size: 1.3rem;
  }

  &:hover {
    box-shadow: 0 4px 6px rgba(253, 100, 0, 0.3);

    ${ImageBackground} {
      transform: scale(1.1);
      transition: transform 6s cubic-bezier(0.25, 0.45, 0.45, 0.95);
    }
  }
`;
